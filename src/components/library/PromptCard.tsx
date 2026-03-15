interface Props {
  number: number;
  title: string;
  onClick: () => void;
}

export default function PromptCard({ number, title, onClick }: Props) {
  const formattedNumber = String(number).padStart(2, '0');

  return (
    <button
      onClick={onClick}
      className="text-left bg-white/5 border border-white/10 rounded-xl p-4 transition-all duration-200 cursor-pointer group hover:border-[#FFD700]/40 hover:shadow-lg hover:shadow-[#FFD700]/5 hover:-translate-y-1 active:scale-[0.98] w-full h-full flex flex-col gap-2"
    >
      <span className="text-[#FFD700] text-xs font-mono font-bold bg-[#FFD700]/10 px-2 py-0.5 rounded w-fit">
        #{formattedNumber}
      </span>
      <h4 className="text-white font-semibold text-sm leading-snug group-hover:text-[#FFD700] transition-colors">
        {title}
      </h4>
    </button>
  );
}
