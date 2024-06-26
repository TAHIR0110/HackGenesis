import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import styled from "styled-components";
import { CgMenu, CgCloseR } from "react-icons/cg";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "../styles/button";
import './Navbar.scss';

const Navbar = () => {
  const [openMenu, setOpenMenu] = useState(false);
  const { user, loginWithRedirect, logout, isAuthenticated } = useAuth0();
  const Nav = styled.nav`
  `;

  return (
    <Nav className="navb">
      <div className={openMenu ? "menuIcon active" : "menuIcon"}>
        <ul className="navbar-list">
          <li>
            <NavLink
              className="navbar-link"
              onClick={() => setOpenMenu(false)}
              to="/"
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              className="navbar-link"
              onClick={() => setOpenMenu(false)}
              to="/about"
            >
              About
            </NavLink>
          </li>
          <li>
            <NavLink
              className="navbar-link"
              onClick={() => setOpenMenu(false)}
              to="/service"
            >
              Disorders
            </NavLink>
          </li>

          <li>
            <NavLink
              className="navbar-link"
              onClick={() => setOpenMenu(false)}
              to="/contact"
            >
              Contact
            </NavLink>
          </li>
          {isAuthenticated && (
            <li>
              <p className="user">Hi {user.name}</p>
            </li>
          )}
          {isAuthenticated ? (
            <li>
              {" "}
              <Button className="login"
                onClick={() =>
                  logout({ logoutParams: { returnTo: window.location.origin } })
                }
              >
                Log Out
              </Button>
            </li>
          ) : (
            <li>
              <Button className="login" onClick={() => loginWithRedirect()}>Log In</Button>;
            </li>
          )}
        </ul>
        {/* //nav icon */}
        <div className="mobile-navbar-btn">
          <CgMenu
            name="menu-outline"
            className="mobile-nav-icon"
            onClick={() => setOpenMenu(true)}
          />
          <CgCloseR
            name="close-outline"
            className="close-outline mobile-nav-icon"
            onClick={() => setOpenMenu(false)}
          />
        </div>
      </div>
    </Nav>
  );
};

export default Navbar;
