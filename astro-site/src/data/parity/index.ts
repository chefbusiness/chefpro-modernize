import type { PageCopy, ParityLang, PromptLang } from './types';
import { CONTACT } from './contact';
import { FAQ } from './faq';
import { ABOUT } from './about';
import { TRAINING } from './training';
import { PROMPTS } from './prompts';

export type { PageCopy, ParityLang, PromptLang } from './types';

export type PageKind = 'contact' | 'faq' | 'about' | 'training' | 'prompts';

export function getPage(kind: PageKind, lang: ParityLang): PageCopy {
  if (kind === 'prompts') {
    if (lang === 'en') {
      throw new Error('The English prompt hub is /en/prompt-libraries, not this entry page.');
    }
    return PROMPTS[lang];
  }
  const table = { contact: CONTACT, faq: FAQ, about: ABOUT, training: TRAINING }[kind];
  return table[lang];
}
