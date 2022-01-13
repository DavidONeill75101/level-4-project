import React from "react"

function Search() {
  const [query, setQuery] = React.useState('')
  const [results,setResults] = React.useState(null)

  const handleClick = async() => {
    const res = await fetch(`http://127.0.0.1:5000/search?query=${query}`)
    const data = await res.json()

    
    setResults(data)
    
    
  }
  if (results){
    return (
      <div>
          <input type="text" placeholder="Search Coronavirus Literature" onChange={event => setQuery(event.target.value)} />    
          <button type="submit" onClick = {handleClick}>Search</button>
          <ul>
            {results.map((result) => (
              <li>{result.docno}</li>
            ))}
          </ul>
      </div>
  
    )
  }else{
    return (
      <div>
          <input type="text" placeholder="Search Coronavirus Literature" onChange={event => setQuery(event.target.value)} />    
          <button type="submit" onClick = {handleClick}>Search</button>
          
      </div>
  
    )
  }
 
}

export default Search