import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  FolderTree, 
  Cpu, 
  GitBranch, 
  Activity, 
  MessageSquareCode, 
  LogOut, 
  ExternalLink 
} from 'lucide-react';

export default function Dashboard() {
  // Initialize state directly from localStorage to prevent setState in useEffect
  const [user] = useState<string>(() => localStorage.getItem('argus_user') || '');
  const [repo] = useState<string>(() => localStorage.getItem('argus_active_repo') || 'https://github.com/example/demo-repo');
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/');
    }
  }, [user, navigate]);

  const handleDisconnect = () => {
    localStorage.removeItem('argus_user');
    localStorage.removeItem('argus_active_repo');
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      {/* Top Navbar */}
      <header className="h-16 border-b border-slate-800/80 px-6 flex items-center justify-between bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2.5 font-bold text-lg tracking-tight text-white">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white text-sm shadow-md shadow-indigo-600/30">
              A
            </div>
            Argus
          </div>
          <span className="text-slate-700">/</span>
          <div className="flex items-center gap-2 text-xs text-slate-400 bg-slate-800/60 px-3 py-1.5 rounded-full border border-slate-700/50">
            <GitBranch className="w-3.5 h-3.5 text-indigo-400" />
            <span className="font-mono text-slate-300">{repo}</span>
          </div>
        </div>

        <div className="flex items-center gap-4 text-xs">
          <div className="flex items-center gap-2 text-slate-400">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            Connected as <span className="text-slate-200 font-medium">{user}</span>
          </div>
          <button
            onClick={handleDisconnect}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors cursor-pointer border border-slate-700/60"
          >
            <LogOut className="w-3.5 h-3.5" />
            <span>Disconnect</span>
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-8 max-w-7xl w-full mx-auto space-y-6">
        {/* Banner */}
        <div className="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/60 via-slate-900 to-slate-900 border border-indigo-900/40 relative overflow-hidden">
          <div className="relative z-10 max-w-2xl">
            <span className="text-xs font-semibold uppercase tracking-wider text-indigo-400 bg-indigo-950 px-2.5 py-1 rounded-md border border-indigo-800/60">
              Phase 0 Complete
            </span>
            <h2 className="text-2xl font-bold text-white mt-3">
              Dashboard Shell Ready
            </h2>
            <p className="text-sm text-slate-400 mt-1.5 leading-relaxed">
              Argus foundation is online. Next up is Phase 1: Ingestion pipeline, AST parsing with Tree-sitter, and LLM-powered module summarization.
            </p>
          </div>
        </div>

        {/* Feature Grid Placeholders */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-slate-700 transition-all group">
            <div>
              <div className="w-10 h-10 rounded-xl bg-indigo-950/80 border border-indigo-800/60 text-indigo-400 flex items-center justify-center mb-4 group-hover:scale-105 transition-transform">
                <FolderTree className="w-5 h-5" />
              </div>
              <h3 className="text-base font-semibold text-slate-200">
                Code Intelligence
              </h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                AST tree-sitter parsing, module dependency graph, and function call graph traversals.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-500">
              <span>Status: Phase 1 & 2</span>
              <Cpu className="w-4 h-4 text-slate-600" />
            </div>
          </div>

          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-slate-700 transition-all group">
            <div>
              <div className="w-10 h-10 rounded-xl bg-violet-950/80 border border-violet-800/60 text-violet-400 flex items-center justify-center mb-4 group-hover:scale-105 transition-transform">
                <Activity className="w-5 h-5" />
              </div>
              <h3 className="text-base font-semibold text-slate-200">
                Process Analytics
              </h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Stale PR detection, turnaround metrics, risk scores, and automated weekly status summaries.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-500">
              <span>Status: Phase 4</span>
              <ExternalLink className="w-4 h-4 text-slate-600" />
            </div>
          </div>

          <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-slate-700 transition-all group">
            <div>
              <div className="w-10 h-10 rounded-xl bg-emerald-950/80 border border-emerald-800/60 text-emerald-400 flex items-center justify-center mb-4 group-hover:scale-105 transition-transform">
                <MessageSquareCode className="w-5 h-5" />
              </div>
              <h3 className="text-base font-semibold text-slate-200">
                RAG Chat & Correlation
              </h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                Vector similarity search via pgvector and automated incident-to-commit root cause correlation.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-500">
              <span>Status: Phase 2 & 6</span>
              <Cpu className="w-4 h-4 text-slate-600" />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
