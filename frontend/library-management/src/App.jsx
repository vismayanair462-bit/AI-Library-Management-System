import { useState,useEffect} from "react";
import { getBooks,addBooks,deleteBooks,updateBooks } from "./services/bookServices";
import axios from 'axios';
import SearchBar from "./components/SearchBar";
import SortButtons from "./components/SortButtons";
import InputPage from "./components/InputPage";
import OutputPage from "./components/OutputPage";

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
      const res = await getBooks();
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
      const res = await addBooks({
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
    const delete_book = window.confirm("Do you want to delete this book?")
    if(!delete_book){
      return;
    }
    setLoading(true);
    setError(null);
    try{
      const res = await deleteBooks(id);
      await getBook();

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
      const res = await updateBooks(id,{
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
      <SearchBar
      search={search}
      setSearch={setSearch}
      >
      </SearchBar>
      <br />
      <SortButtons
        setSortBy={setSortBy}
        setSortRating={setSortRating}
        sortRating={sortRating}
        setSortTitle={setSortTitle}
        sortTitle={sortTitle}
        showAvailable={showAvailable}
        setShowAvailable={setShowAvailable}
      >
      </SortButtons>
      <br />
     <InputPage
     formData={formData}
     setFormData={setFormData}
     addBook={addBook}
     >
     </InputPage>
      {loading && <p>LOADING....</p>}
      {error && <p>{error}</p>}
      <ul>
       <OutputPage
       sortBooks={sortBooks}
       updateID={updateID}
       editText={editText}
       setEditText={setEditText}
       updateBook={updateBook}
       setUpdateID={setUpdateID}
       deleteBook={deleteBook}
       startEdit={startEdit}
       >
       </OutputPage>
      </ul>
    </div>

  );
}
export default App;