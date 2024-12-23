import { BrowserRouter, Routes, Route, Link, Navigate } from 'react-router-dom';
import MyComponent from './features/todo/services/Todo'
import Home from './features/todo';

function About() {
  return <h2>About</h2>;
}

function Contact() {
  return <h2>Contact</h2>;
}

function NoMatch() {
  return <h2>404 Not Found</h2>;
}

function App() {
  return (
    <BrowserRouter>
      {/* <nav> */}
        {/* <ul> */}
          {/* <li>
            <Link to="/">Home</Link>
          </li> */}
          {/* <li> */}
            {/* <Link to="/about">About</Link> */}
          {/* </li> */}
          {/* <li> */}
            {/* <Link to="/contact">Contact</Link> */}
          {/* </li> */}
        {/* </ul> */}
      {/* </nav> */}

      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/" element={<Home />} /> */}
        {/* <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*" element={<NoMatch />} /> {/* Маршрут по умолчанию для ошибок 404 */}
        {/* <Route path="/redirect" element={<Navigate replace to="/about" />} /> Перенаправление */} 
      </Routes>
    </BrowserRouter>
  );
}

export default App;
