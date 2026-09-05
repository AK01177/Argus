import { useState, useEffect } from "react";
import { FileCode2, Sparkles, FolderTree } from "lucide-react";

interface FileNode {
  path: string;
  summary: string | null;
}

export default function FileTree({ repoId }: { repoId: number }) {
  const [files, setFiles] = useState<FileNode[]>([]);
  const [loading, setLoading] = useState(true);
  const [hoveredSummary, setHoveredSummary] = useState<string | null>(null);
  const [activeFile, setActiveFile] = useState<string | null>(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/repos/${repoId}/tree`)
      .then((res) => res.json())
      .then((data) => {
        setFiles(data.files);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch tree:", err);
        setLoading(false);
      });
  }, [repoId]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64 bg-slate-900/40 border border-slate-800 rounded-2xl animate-pulse">
        <span className="text-slate-400 flex items-center gap-2">
          <FolderTree className="w-5 h-5" />
          Loading repository structure...
        </span>
      </div>
    );
  }

  if (files.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-64 bg-slate-900/40 border border-slate-800 rounded-2xl">
        <FolderTree className="w-8 h-8 text-slate-600 mb-3" />
        <span className="text-slate-400">No files found for this repo yet.</span>
      </div>
    );
  }

  return (
    <div className="flex flex-col md:flex-row gap-6 h-[500px]">
      
      {/* --- Left: File Explorer Panel --- */}
      <div className="w-full md:w-1/2 flex flex-col bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden shadow-xl shadow-black/20">
        <div className="px-5 py-4 border-b border-slate-800/80 bg-slate-900/80 flex items-center gap-2">
          <FolderTree className="w-4 h-4 text-indigo-400" />
          <h3 className="font-semibold text-slate-200 text-sm">Repository Files</h3>
        </div>
        
        <ul className="flex-1 overflow-y-auto p-3 space-y-1 custom-scrollbar">
          {files.map((file, index) => (
            <li
              key={index}
              className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-all duration-200 text-sm font-mono
                ${activeFile === file.path 
                  ? "bg-indigo-600/10 border border-indigo-500/30 text-indigo-300" 
                  : "border border-transparent text-slate-400 hover:bg-slate-800/60 hover:text-slate-200"
                }
              `}
              onMouseEnter={() => {
                setHoveredSummary(file.summary);
                setActiveFile(file.path);
              }}
              onMouseLeave={() => {
                setHoveredSummary(null);
                setActiveFile(null);
              }}
            >
              <FileCode2 className={`w-4 h-4 ${activeFile === file.path ? "text-indigo-400" : "text-slate-600"}`} />
              <span className="truncate">{file.path}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* --- Right: AI Summary Tooltip Panel --- */}
      <div className="w-full md:w-1/2 flex flex-col bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden shadow-xl shadow-black/20 relative group transition-all">
        {/* Glow effect in background */}
        <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-600/5 rounded-full blur-3xl -z-10 transition-opacity"></div>
        
        <div className="px-5 py-4 border-b border-slate-800/80 bg-slate-900/80 flex items-center gap-2">
          <Sparkles className="w-4 h-4 text-emerald-400" />
          <h3 className="font-semibold text-slate-200 text-sm">Gemini Analysis</h3>
        </div>

        <div className="flex-1 p-6 overflow-y-auto">
          {hoveredSummary ? (
            <div className="animate-in fade-in slide-in-from-bottom-2 duration-300">
              <p className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap">
                {hoveredSummary}
              </p>
            </div>
          ) : (
            <div className="h-full flex flex-col items-center justify-center text-center opacity-60">
              <Sparkles className="w-10 h-10 text-slate-600 mb-4" />
              <p className="text-slate-500 text-sm max-w-[200px]">
                Hover over any file to reveal its AI-generated summary.
              </p>
            </div>
          )}
        </div>
      </div>

    </div>
  );
}
