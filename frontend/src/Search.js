import React, { useState } from 'react';
import axios from 'axios';

const Search = () => {
  const [city, setCity] = useState('');
  const [news, setNews] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:5000/search', { city });
    setNews(response.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={city} 
          onChange={(e) => setCity(e.target.value)} 
        />
        <button type="submit">Search</button>
      </form>
      
      <div>
        {news.map((item, index) => (
          <div key={index}>
            <h3>{item.title}</h3>
            <p>{item.summary}</p>
            <a href={item.link} >Read more</a>
          </div>
        ))}
      </div>

    </div>
  );
};

export default Search;
