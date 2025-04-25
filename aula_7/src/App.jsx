import './App.css'
import { Route, Routes } from 'react-router'
import Home from './pages/Home'
import DashBoard from './pages/DashBoard'

function App() {
  return (
    <Routes>
      <Route index element={<Home />} />
      <Route path='/dash' element={<DashBoard />} />
    </Routes>
  )
}

export default App
