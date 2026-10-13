import axios from 'axios';

 const BASE_URL = 'http://127.0.0.1:8000/book';

/* API to get all the books from the system */
 export const getBooks=()=>axios.get(BASE_URL)

/* API to add new book into the system */ 
export const addBooks=(book)=>axios.post(BASE_URL,book);

/* API to delete a book from the system */
export const deleteBooks=(id)=>axios.delete(`${BASE_URL}/${id}`);

/* API to update the book details in the system */
export const updateBooks=(id,book)=>axios.put(`${BASE_URL}/${id}`,book)