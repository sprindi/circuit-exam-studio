#!/usr/bin/env python3
"""Serve only the study app, using the Python standard library."""
import argparse
import re
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

class StudyHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(404, 'Not found')
        return None

    def send_head(self):
        parts = Path(unquote(urlsplit(self.path).path)).parts
        if any(part.startswith('.') or part == '..' for part in parts):
            self.send_error(404, 'Not found')
            return None
        target = Path(self.translate_path(self.path)).resolve()
        if not target.is_relative_to(Path(self.directory).resolve()):
            self.send_error(404, 'Not found')
            return None
        if target.is_file() and target.suffix.lower() == '.mp4':
            source = target.open('rb')
            size = target.stat().st_size
            byte_range = self.headers.get('Range')
            start, end = 0, size - 1
            if byte_range:
                match = re.fullmatch(r'bytes=(\d*)-(\d*)', byte_range.strip())
                if not match or not any(match.groups()):
                    source.close()
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{size}')
                    self.send_header('Content-Length', '0')
                    self.end_headers()
                    return None
                left, right = match.groups()
                if left:
                    start = int(left)
                    end = min(int(right), size - 1) if right else size - 1
                else:
                    length = int(right)
                    start = max(0, size - length)
                    if length == 0:
                        start = size
                if start >= size or end < start:
                    source.close()
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{size}')
                    self.send_header('Content-Length', '0')
                    self.end_headers()
                    return None
            self.send_response(206 if byte_range else 200)
            self.send_header('Content-Type', 'video/mp4')
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Length', str(end - start + 1))
            self.send_header('Last-Modified', self.date_time_string(target.stat().st_mtime))
            if byte_range:
                self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
            self.end_headers()
            source.seek(start)
            self._video_remaining = end - start + 1
            return source
        return super().send_head()

    def copyfile(self, source, outputfile):
        remaining = getattr(self, '_video_remaining', None)
        if remaining is None:
            return super().copyfile(source, outputfile)
        try:
            while remaining > 0:
                block = source.read(min(256 * 1024, remaining))
                if not block:
                    break
                outputfile.write(block)
                remaining -= len(block)
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            del self._video_remaining

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bind', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent/'dist')
    args = parser.parse_args()
    folder = args.directory.resolve()
    if not (folder/'index.html').is_file():
        parser.error(f'No index.html in {folder}')
    server = ThreadingHTTPServer((args.bind, args.port), partial(StudyHandler, directory=str(folder)))
    print(f'Circuit Exam Studio: http://{args.bind}:{args.port}/', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
