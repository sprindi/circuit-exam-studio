import {z} from 'zod';
import raw from './lessons.json';
const symbol=z.tuple([z.string().min(1),z.string().min(1)]);
const phase=z.object({title:z.string(),equation:z.string(),why:z.string(),voice:z.string(),audio:z.string().optional()});
const rule=z.object({formula:z.string(),when:z.string(),symbols:z.array(symbol)});
const scene=z.object({id:z.string(),title:z.string(),purpose:z.string(),paragraphs:z.array(z.string()).min(1),visual:z.enum(['physical','purposes','network','load','charge','potential','emf','power','energy','quantities','conditions','balance']),rule:rule.optional(),phases:z.array(phase).optional(),condition:z.enum(['loaded','open','short']).optional(),takeaway:z.string(),voice:z.string(),audio:z.string().optional(),source:z.string(),note:z.string().optional()});
const lesson=z.object({title:z.string(),question:z.string(),preparation:z.array(z.string()),prerequisite:z.object({topic:z.string(),label:z.string()}).optional(),goals:z.array(z.object({id:z.string(),text:z.string()})),scenes:z.array(scene).min(2),finish:z.string()});
export const lessons=z.record(z.string(),lesson).parse(raw);
export type Lesson=z.infer<typeof lesson>;export type Scene=z.infer<typeof scene>;export type Phase=z.infer<typeof phase>;
