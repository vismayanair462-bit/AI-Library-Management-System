function InputPage({formData,setFormData,addBook}){
    return(
        <>
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
        </>
    );
}
export default InputPage;