import React from "react";
import { NavLink } from "react-router-dom";
import Navbar from "./Navbar";
import styled from "styled-components";
import "./Header.css";

const Header = () => {
  return (
    <MainHeader>
      <NavLink to="/">
        <h1 className="logo">Medistats.</h1>
      </NavLink>
      <Navbar />
    </MainHeader>
  );
};
const MainHeader = styled.header`
  padding: 1.3rem 4.4rem;
  // margin-top: 0.5rem
  height: 6.5rem;
  background-color: #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: "Poppins", sans-serif;
`;
export default Header;
