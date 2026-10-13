function OutputPage({sortBooks,updateID,editText,setEditText,updateBook,setUpdateID,deleteBook,startEdit}){
    return(
        <>
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
        </>
    );
}
export default OutputPage;