import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import MainPage from './pages/mainpage/MainPage.jsx';
import SC_Page from './pages/sc_page/SC_Page';

function App()
{
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/classify-emotion" element={<MainPage />} />
        <Route path="/classify-sentence" element={<SC_Page />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
