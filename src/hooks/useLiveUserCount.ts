/**
 * useLiveUserCount
 *
 * Returns a deterministic, ever-growing user count.
 * Starting from BASE_COUNT on BASE_DATE, adds DAILY_INCREMENT each day.
 * No backend required — same value for every visitor on the same day.
 */

const BASE_DATE = new Date('2026-03-01');
const BASE_COUNT = 4847;
const DAILY_INCREMENT = 25;

function getRawCount(): number {
  const today = new Date();
  const diffMs = today.getTime() - BASE_DATE.getTime();
  const diffDays = Math.max(0, Math.floor(diffMs / (1000 * 60 * 60 * 24)));
  // Add a small deterministic variation per day (±3) so consecutive days
  // don't all add exactly 25 — feels more organic.
  let total = BASE_COUNT;
  for (let i = 1; i <= diffDays; i++) {
    const variation = ((i * 7 + 3) % 7) - 3; // -3 to +3
    total += DAILY_INCREMENT + variation;
  }
  return total;
}

/**
 * Returns the current user count formatted for the given locale.
 * Examples: 4.872 (es), 4,872 (en)
 */
export function useLiveUserCount(locale: string = 'es'): {
  count: number;
  formatted: string;
  formattedPlus: string;
} {
  const count = getRawCount();
  const formatted = count.toLocaleString(locale === 'en' ? 'en-US' : 'es-ES');
  return {
    count,
    formatted,
    formattedPlus: `${formatted}+`,
  };
}
