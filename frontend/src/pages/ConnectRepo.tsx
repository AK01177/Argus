import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { KeyRound, ArrowRight, ShieldCheck, Sparkles, GitBranch } from 'lucide-react';


export default function ConnectRepo() {
  const [username, setUsername] = useState('');
  const [githubPat, setGithubPat] = useState('');
  const [repoUrl, setRepoUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const navigate = useNavigate();

  const handleConnect = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/auth/pat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username.trim(),
          github_pat: githubPat.trim(),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to connect account');
      }

      localStorage.setItem('argus_user', username);
      if (repoUrl) {
        localStorage.setItem('argus_active_repo', repoUrl);
      }

      navigate('/dashboard');
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unexpected error occurred. Make sure your backend is running on port 8000.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center justify-center p-6 selection:bg-indigo-500 selection:text-white">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.15),rgba(255,255,255,0))] pointer-events-none" />

      <div className="w-full max-w-lg relative z-10">
        {/* Brand Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-tr from-indigo-600 to-violet-500 text-white shadow-lg shadow-indigo-500/25 mb-4 ring-1 ring-white/20">
            <Sparkles className="w-7 h-7" />
          </div>
          <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
            Argus
          </h1>
          <p className="text-sm text-slate-400 mt-2">
            Engineering Intelligence Platform — Code, Process & Ops
          </p>
        </div>

        {/* Card */}
        <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-2xl p-8 shadow-2xl ring-1 ring-white/5">
          <div className="mb-6">
            <h2 className="text-lg font-semibold text-slate-200 flex items-center gap-2">
              <GitBranch className="w-5 h-5 text-indigo-400" /> Connect Your Repository
            </h2>
            <p className="text-xs text-slate-400 mt-1">
              Provide your GitHub Personal Access Token to index and analyze repository architecture.
            </p>
          </div>

          {error && (
            <div className="mb-5 p-3 rounded-lg bg-red-950/50 border border-red-800/60 text-red-300 text-xs flex items-center gap-2">
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleConnect} className="space-y-4">
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1.5">
                Username
              </label>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="e.g. dev-aryan"
                className="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
              />
            </div>

            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1.5 flex items-center justify-between">
                <span>GitHub Personal Access Token (PAT)</span>
                <span className="text-[11px] text-slate-500 font-normal">Starts with ghp_</span>
              </label>
              <div className="relative">
                <input
                  type="password"
                  required
                  value={githubPat}
                  onChange={(e) => setGithubPat(e.target.value)}
                  placeholder="ghp_xxxxxxxxxxxxxxxxxxxx"
                  className="w-full pl-9 pr-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                />
                <KeyRound className="w-4 h-4 text-slate-500 absolute left-3 top-3" />
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1.5">
                Target GitHub Repo URL <span className="text-slate-500 font-normal">(Optional for now)</span>
              </label>
              <input
                type="text"
                value={repoUrl}
                onChange={(e) => setRepoUrl(e.target.value)}
                placeholder="https://github.com/owner/repository"
                className="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full mt-2 py-2.5 px-4 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm flex items-center justify-center gap-2 shadow-lg shadow-indigo-600/25 transition-all disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
            >
              {loading ? (
                <span>Connecting...</span>
              ) : (
                <>
                  <span>Connect & Enter Dashboard</span>
                  <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </form>

          <div className="mt-6 pt-5 border-t border-slate-800/80 flex items-center justify-center gap-1.5 text-xs text-slate-500">
            <ShieldCheck className="w-4 h-4 text-emerald-500" />
            <span>Tokens are securely stored in PostgreSQL.</span>
          </div>
        </div>
      </div>
    </div>
  );
}
