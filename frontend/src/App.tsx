import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ConnectRepo from './pages/ConnectRepo';
import Dashboard from './pages/Dashboard';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ConnectRepo />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}
