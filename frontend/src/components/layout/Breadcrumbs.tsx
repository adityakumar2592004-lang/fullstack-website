import React from 'react';
import { ChevronRight, Home } from 'lucide-react';

interface BreadcrumbsProps {
  items: {
    label: string;
    onClick?: () => void;
  }[];
}

export const Breadcrumbs: React.FC<BreadcrumbsProps> = ({ items }) => {
  return (
    <nav className="flex items-center space-x-1.5 text-xs text-slate-400 py-3 px-4 sm:px-6 lg:px-8 border-b border-slate-800/80 bg-slate-950/40">
      <button
        onClick={items[0]?.onClick}
        className="flex items-center hover:text-white transition-colors"
      >
        <Home className="w-3.5 h-3.5" />
      </button>
      {items.map((item, index) => (
        <React.Fragment key={index}>
          <ChevronRight className="w-3 h-3 text-slate-600 shrink-0" />
          {item.onClick ? (
            <button
              onClick={item.onClick}
              className="hover:text-blue-400 font-medium transition-colors truncate max-w-[200px]"
            >
              {item.label}
            </button>
          ) : (
            <span className="text-slate-200 font-semibold truncate max-w-[250px]">
              {item.label}
            </span>
          )}
        </React.Fragment>
      ))}
    </nav>
  );
};
