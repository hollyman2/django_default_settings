import React, { useState, useEffect } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/'); // Замените на ваш endpoint
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // Пустой массив [] гарантирует, что запрос выполняется только один раз после монтирования компонента

  if (loading) {
    return <p>Загрузка данных...</p>;
  }

  if (error) {
    return <p>Ошибка: {error.message}</p>;
  }

  if (!data) {
    return <p>Нет данных.</p>; // Дополнительная проверка на случай отсутствия данных
  }

  return (
    <div>
      <h2>Полученные данные:</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre> {/* Вывод данных в формате JSON */}
      {/* Или, если у вас структурированные данные, например, массив объектов: */}
      <h1>{data.message}</h1>

        </div>
      )} 
    


export default MyComponent;
