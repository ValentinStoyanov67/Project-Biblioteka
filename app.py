import streamlit as st
st.title("Моята библиотека")
st.write("Добре дошли в моята дигитална библиотека!")
import streamlit as st
st.title("Моята библиотека")
books = [    "Хари Потър",    "Малкият принц",    "Хобит",    "1984",    "Под игото"]
st.subheader("Всички книги")
for book in books:    
  st.write("📖", book)
  new_book = st.text_input("Въведете заглавие на книга")

if st.button("Добави книга"):

    if new_book != "":

        books.append(new_book)

        st.success("Книгата е добавена!")

    else:

        st.warning("Моля, въведете заглавие!")
      if "books" not in st.session_state:    
st.session_state.books = ["Хари Потър","Малкият принц","Хобит", "1984", "Под игото"]
st.session_state.books
st.session_state.books.append(new_book)
st.subheader("📖 Всички книги")
for book in st.session_state.books:    
  st.write(book)
st.subheader("Търсене на книга")
search = st.text_input("Каква книга търсите?")
if st.button("Търси"):    
  found = False    
for book in st.session_state.books:        
  if search.lower() in book.lower():            
    st.success("Намерена книга: " + book)            
    found = True    
  if found == False:        
    st.warning("Няма такава книга!")
st.subheader("Изтриване на книга")
if len(st.session_state.books) > 0:    
selected_book = st.selectbox(        "Изберете книга:",        st.session_state.books    )    if st.button("Изтрий"):        
st.session_state.books.remove(selected_book)        
st.success("Книгата е изтрита!")        
st.rerun()else:    
st.info("Библиотеката е празна!")
st.subheader(" Сортиране")
if st.button("Сортирай по азбучен ред"):    
st.session_state.books.sort()    
st.rerun()
st.subheader("Статистика")
total = len(st.session_state.books)
st.metric("Общ брой книги", total)
st.subheader("Препоръчани книги")col1, col2, col3 = st.columns(3)with col1:    st.image("https://covers.openlibrary.org/b/isbn/9780747532699-M.jpg")    
st.write("Хари Потър")with col2:    st.image("https://covers.openlibrary.org/b/isbn/9780156012195-M.jpg")    
st.write("Малкият принц")with col3:    st.image("https://covers.openlibrary.org/b/isbn/9780547928227-M.jpg")    
