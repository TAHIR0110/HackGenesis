import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
*{
    margin:0;
    padding:0;
    box-sizing: border-box;
    font-family:'Work Sans',sans-serif;
    position:fix;
}
html{
 font-size:62.5%;
 overflow-x:hidden;
}

body {
  overflow-x: hidden;
   scrollbar-color: rgb(98 84 243);
    scrollbar-width: thin;
}
body::-webkit-scrollbar {
  width: 1.5rem;
}
body::-webkit-scrollbar-track {
   background-color: rgb(24 24 29);
}
body::-webkit-scrollbar-thumb {
 
  background: #fff;
    border: 5px solid transparent;
    border-radius: 9px;
    background-clip: content-box;
}


h1{
    color:${({ theme }) => theme.colors.heading};
    font-size:6rem;
    font-weight:900;
}
h2{
    color:#444;
    font-size: 3rem;
    font-weight:bolder;
    white-space:normal;
    text-align:center;
}
h3 {
    font-size: 1.8rem;
    font-weight: 400;
  }

  p {
    color: ${({ theme }) => theme.colors.text};
    opacity: .7;
    font-size: 1.65rem;
    line-height: 1.5;
    margin-top: 1rem;
    font-weight:400;
  }
  a {
    text-decoration: none;
  }
  li {
    list-style: none;
  }
  .container {
    max-width: 120rem;
    margin: 0 auto;
  }
  .grid {
    display: grid;
    gap: 9rem;
  }
  .grid-two-column {
    grid-template-columns: repeat(2, 1fr);
  }
  .grid-three-column {
    grid-template-columns: repeat(3, 1fr);
  }
  .grid-four-column{
     grid-template-columns: 1fr 1.2fr .5fr .8fr ;
  }
  
  input, textarea{
  max-width: 50rem;
  color: ${({ theme }) => theme.colors.black};
  padding: 1.6rem 2.4rem;
  border: 1px solid ${({ theme }) => theme.colors.border};
  text-transform: uppercase;
 box-shadow: ${({ theme }) => theme.colors.shadowSupport};
}
  input[type="submit"]{
  max-width: 16rem;
  margin-top: 2rem;
  background-color: #3796bb; ;
  color: ${({ theme }) => theme.colors.white};
  padding: 1.4rem 2.2rem;
  border-style: solid;
  border-width: .1rem;
  text-transform: uppercase;
  font-size: 1.8rem;
  cursor: pointer;
  }
  
@media (max-width:${({ theme }) => theme.media.tab}) {
      .container{
        padding: 0 3.2rem;
      }
        .grid-three-column {
      grid-template-columns: 1fr 1fr;
    }
}
@media (max-width:${({ theme }) => theme.media.mobile}) {
      html{
        font-size: 50%;
      }
      .grid{
        gap: 3.2rem;
      }
      .grid-two-column, .grid-three-column, .grid-four-column{
        grid-template-columns: 1fr;
      }
}
`;
