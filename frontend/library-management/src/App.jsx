import { useState,useEffect, use } from "react";
import axios from 'axios';

function App(){
  const[formData,setFormData] = useState({
    title:"",
    author:"",
    publication_year:"",
    genre:"",
    rating:"",
    language:"",
    available:false
  });
  const[response,setResponse] = useState([]);
  const[error,setError] = useState(null);
  const[loading,setLoading] = useState(false);
  const[search,setSearch] = useState("");
  const[sortBy,setSortBy] = useState('title');
  const[sortTitle,setSortTitle] = useState('A-Z');
  const[sortRating,setSortRating] = useState('highest-lowest');
  const[showAvailable,setShowAvailable] = useState(false);
  const[updateID,setUpdateID] = useState(null);
  const[editText,setEditText] = useState({
      title:"",
      author:"",
      publication_year:"",
      genre:"",
      rating:"",
      language:"",
      available:false
  });

  const BASE_URL = 'http://127.0.0.1:8000';

  /* Function to get all the books from the system */
  const getBook=async()=>{
    setLoading(true);
    setError(false);
    try{
      const res = await axios.get(`${BASE_URL}/book`);
      setResponse(res.data);
    }
    catch(err){
      setError(err.response?.data?.detail||
        "Something went wrong."
      );
    }
    finally{
      setLoading(false);
    }
  }

  /* Function to add new books into the system */
  const addBook=async()=>{
    setLoading(true);
    setError(null);
    if(!formData.title.trim()||!formData.author.trim()||!formData.publication_year||!formData.genre.trim()||!formData.rating||!formData.language.trim()){
      alert("Please fill the necessary details.");
      return;
    }
    if(formData.publication_year<1000){
      alert("Please fill a valid year.");
      return;
    }
    if(formData.rating < 0 || formData.rating > 5){
      alert("Rating must be between 0 and 5.");
      return;
    }
    try{
      const res = await axios.post(`${BASE_URL}/book`,{
        title:formData.title,
        author:formData.author,
        publication_year:Number(formData.publication_year),
        genre:formData.genre,
        rating:Number(formData.rating),
        language:formData.language,
        available:formData.available
      });
      await getBook();
      alert(res.data.message);
      setFormData({
          title:"",
          author:"",
          publication_year:"",
          genre:"",
          rating:"",
          language:"",
          available:false
      });
    }
    catch(err){
      setError(err.response?.data?.detail||
        "Something went wrong."
      );
    }
    finally{
      setLoading(false);
    }
  }

  /* Function to delete a book from the system */ 
  const deleteBook=async(id)=>{
    setLoading(true);
    setError(null);

    const delete_book = window.confirm("Do you want to delete this book?")
    if(!delete_book){
      return;
    }
    try{
      const res = await axios.delete(`${BASE_URL}/book/${id}`);
      getBook();
      alert(res.data.message);
    }
    catch(err){
      setError(err.response?.data?.detail||
        "Something went wrong."
      );
    }
    finally{
      setLoading(false);
    }
  }

  /* Function to filter title, author,genre,language and availability of a book in the system */
  const filterBook = response.filter((book)=>{
    const matchSearch = 
      (book.title.toLowerCase().includes(search.toLowerCase()))||
      (book.author.toLowerCase().includes(search.toLowerCase()))||
      (book.genre.toLowerCase().includes(search.toLowerCase()))||
      (book.language.toLowerCase().includes(search.toLowerCase()));

    const availableSearch = 
      (book.available||!showAvailable);

    return matchSearch && availableSearch
  });

  /* Function for sorting books by title and rating */
  const sortBooks = [...filterBook].sort((a,b)=>{
    if(sortBy==='title'){
      if(sortTitle==='A-Z'){
        return a.title.localeCompare(b.title);
      }
      if(sortTitle==='Z-A'){
        return b.title.localeCompare(a.title);
      }
    }
    if(sortBy==='rating'){
      if(sortRating==='highest-lowest'){
        return b.rating - a.rating;
      }
      if(sortRating==='lowest-highest'){
        return a.rating - b.rating;
      }
    }
  });

  /* Function to allow users to edit book details in the system */
  const startEdit=(book)=>{
    setUpdateID(book.id);
    setEditText({
      title:book.title,
      author:book.author,
      publication_year:book.publication_year,
      genre:book.genre,
      rating:book.rating,
      language:book.language,
      available:book.available
    });
  }

  /* Function to update the details of a book in the system */ 
  const updateBook=async(id)=>{
    setLoading(true);
    setError(null);
    try{
      const res = await axios.put(`${BASE_URL}/book/${id}`,{
          title:editText.title,
          author:editText.author,
          publication_year:editText.publication_year,
          genre:editText.genre,
          rating:editText.rating,
          language:editText.language,
          available:editText.available
      });
      await getBook();
      alert(res.data.message);
      setUpdateID(null);
    }
    catch(err){
      setError(err.response?.data?.detail||
        'something went wrong.'
      );
    }
    finally{
      setLoading(false);
    }
  }

  useEffect(()=>{
    getBook();
  },[]);

  return(
    <div>
      <h1>Library Management System</h1>
      <br />
      <input placeholder="SEARCH..." value={search} onChange={(e)=>setSearch(e.target.value)} />
      <br />
      <button onClick={()=>{
        setSortBy('title');
        setSortTitle(sortTitle==='A-Z'?'Z-A':'A-Z')
      }}>
        {sortTitle}
      </button>
      <button onClick={()=>{
        setSortBy('rating');
        setSortRating(sortRating==='highest-lowest'?'lowest-highest':'highest-lowest')
      }}>
        {sortRating==='highest-lowest'?'Lowest-Highest':'Highest-Lowest'}
      </button>
      <button onClick={()=>{
        setShowAvailable(!showAvailable)
      }}>
        {showAvailable?'All Books':'Available Books'}
      </button>
      <br />
      <input placeholder="Enter title" value={formData.title} onChange={(e)=>setFormData({...formData,title:e.target.value})} />
      <br />
      <input placeholder="Enter author" value={formData.author} onChange={(e)=>setFormData({...formData,author:e.target.value})} />
      <br />
      <input min="1000" placeholder="Enter publication year" value={formData.publication_year} onChange={(e)=>setFormData({...formData,publication_year:e.target.value})} />
      <br />
      <select value={formData.genre} onChange={(e)=>setFormData({...formData,genre:e.target.value})}>
          <option value="">Select Genre</option>
          <option value="Fiction">Fiction</option>
          <option value="Non-Fiction">Non-Fiction</option>
          <option value="Fantasy">Fantasy</option>
          <option value="Science Fiction">Science Fiction</option>
          <option value="Mystery">Mystery</option>
          <option value="Thriller">Thriller</option>
          <option value="Romance">Romance</option>
          <option value="Horror">Horror</option>
          <option value="Historical Fiction">Historical Fiction</option>
          <option value="Biography">Biography</option>
          <option value="Autobiography">Autobiography</option>
          <option value="Self-Help">Self-Help</option>
          <option value="Philosophy">Philosophy</option>
          <option value="Science">Science</option>
          <option value="Technology">Technology</option>
          <option value="Adventure">Adventure</option>
          <option value="Comedy">Comedy</option>
          <option value="Drama">Drama</option>
          <option value="Poetry">Poetry</option>
          <option value="Comics & Graphic Novels">Comics &amp; Graphic Novels</option>
      </select>
      <br />
      <label>
         Rating:
        <input type="number" min="1" max="5" value={formData.rating} onChange={(e)=>setFormData({...formData,rating:e.target.value})} />
      </label>
      <br />
      <select value={formData.language} onChange={(e)=>setFormData({...formData,language:e.target.value})}>
          <option value="">Select Language</option>
          <option value="English">English</option>
          <option value="Tamil">Tamil</option>
          <option value="Hindi">Hindi</option>
          <option value="Malayalam">Malayalam</option>
          <option value="Telugu">Telugu</option>
          <option value="Kannada">Kannada</option>
          <option value="Bengali">Bengali</option>
          <option value="Marathi">Marathi</option>
          <option value="Gujarati">Gujarati</option>
          <option value="Punjabi">Punjabi</option>
          <option value="Urdu">Urdu</option>
          <option value="Sanskrit">Sanskrit</option>
          <option value="French">French</option>
          <option value="Spanish">Spanish</option>
          <option value="German">German</option>
          <option value="Italian">Italian</option>
          <option value="Portuguese">Portuguese</option>
          <option value="Japanese">Japanese</option>
          <option value="Chinese">Chinese</option>
          <option value="Korean">Korean</option>
          <option value="Arabic">Arabic</option>
          <option value="Russian">Russian</option>
      </select>
      <br />
      <label>
         Book Availbility:
        <input type="checkbox" checked={formData.available} onChange={(e)=>setFormData({...formData,available:e.target.checked})}></input>
      </label>
      <br />
      <button onClick={addBook}>Add Book</button>
      {loading && <p>LOADING....</p>}
      {error && <p>{error}</p>}
      <ul>
        {sortBooks.map((book)=>(
          <li key={book.id}>
            {updateID===book.id?(
              <>
                <input placeholder="Enter title" value={editText.title} onChange={(e)=>setEditText({...editText,title:e.target.value})} />
                <input placeholder="Enter author" value={editText.author} onChange={(e)=>setEditText({...editText,author:e.target.value})} />
                <input min="1000" placeholder="Enter publication year" value={editText.publication_year} onChange={(e)=>setEditText({...editText,publication_year:e.target.value})} />
                <select value={editText.genre} onChange={(e)=>setEditText({...editText,genre:e.target.value})}>
                    <option value="">Select Genre</option>
                    <option value="Fiction">Fiction</option>
                    <option value="Non-Fiction">Non-Fiction</option>
                    <option value="Fantasy">Fantasy</option>
                    <option value="Science Fiction">Science Fiction</option>
                    <option value="Mystery">Mystery</option>
                    <option value="Thriller">Thriller</option>
                    <option value="Romance">Romance</option>
                    <option value="Horror">Horror</option>
                    <option value="Historical Fiction">Historical Fiction</option>
                    <option value="Biography">Biography</option>
                    <option value="Autobiography">Autobiography</option>
                    <option value="Self-Help">Self-Help</option>
                    <option value="Philosophy">Philosophy</option>
                    <option value="Science">Science</option>
                    <option value="Technology">Technology</option>
                    <option value="Adventure">Adventure</option>
                    <option value="Comedy">Comedy</option>
                    <option value="Drama">Drama</option>
                    <option value="Poetry">Poetry</option>
                    <option value="Comics & Graphic Novels">Comics &amp; Graphic Novels</option>
                </select>
                <label>
                  Rating:
                   <input type="number" min="1" max="5" value={editText.rating} onChange={(e)=>setEditText({...editText,rating:e.target.value})} />
                </label>
                <select value={editText.language} onCanPlay={(e)=>setEditText({...editText,language:e.target.value})}>
                    <option value="">Select Language</option>
                    <option value="English">English</option>
                    <option value="Tamil">Tamil</option>
                    <option value="Hindi">Hindi</option>
                    <option value="Malayalam">Malayalam</option>
                    <option value="Telugu">Telugu</option>
                    <option value="Kannada">Kannada</option>
                    <option value="Bengali">Bengali</option>
                    <option value="Marathi">Marathi</option>
                    <option value="Gujarati">Gujarati</option>
                    <option value="Punjabi">Punjabi</option>
                    <option value="Urdu">Urdu</option>
                    <option value="Sanskrit">Sanskrit</option>
                    <option value="French">French</option>
                    <option value="Spanish">Spanish</option>
                    <option value="German">German</option>
                    <option value="Italian">Italian</option>
                    <option value="Portuguese">Portuguese</option>
                    <option value="Japanese">Japanese</option>
                    <option value="Chinese">Chinese</option>
                    <option value="Korean">Korean</option>
                    <option value="Arabic">Arabic</option>
                    <option value="Russian">Russian</option>
                </select>
                 <label>
                   Book Availbility:
                  <input type="checkbox" checked={editText.available} onChange={(e)=>setEditText({...editText,available:e.target.checked})}></input>
                </label>
                <button onClick={()=>updateBook(book.id)}>Save Changes</button>
                <button onClick={()=>setUpdateID(null)}>Cancel</button>
              </>
              ):(
                <>
                <h4>{book.title} by {book.author}({book.language}):{book.genre}</h4>
                <p>publication year:{book.publication_year}</p>
                <p>Rating:{book.rating}</p>
                <button onClick={()=>deleteBook(book.id)}>Delete Book</button>
                <button onClick={()=>startEdit(book)}>Update Book</button>
                </>
              )}
          </li>
        ))}
      </ul>
    </div>

  );
}
export default App;