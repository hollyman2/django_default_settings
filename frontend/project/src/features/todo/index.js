import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MyComponent from './services/Todo';
function NoMatch() {
  return <h2>404 Nцвйвцвйвot Found: <MyComponent/></h2>;
}
function Home() {
  return (
  
    <Routes>
      <Route path="" element={<NoMatch />} /> 
      
    </Routes>
  
  );
}

export default Home;
