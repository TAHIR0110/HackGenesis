import React from "react";
import styled from "styled-components";
import { NavLink } from "react-router-dom";
import { Button } from "../styles/button";
import './Footer.scss'
import { FaDiscord, FaInstagram, FaLinkedin } from "react-icons/fa";
const Footer = () => {
  return (
    <Wrapper>
      <section className="contact-short">
        <div className="grid grid-two-column">
          <div>
            <h3>Ready to Solve Your Problem?</h3>
            <h3>Talk to us today</h3>
          </div>
          <div>
            <NavLink to="/">
              <button className="butn" >Get Started</button>
            </NavLink>
          </div>
        </div>
      </section>
      {/* footer section */}
      <footer className="footer">
        <div className="container grid grid-four-column">
          <div className="footer-about">
            <h3>Medistats is here for you</h3>
            <p>
            Feel Free to contact us if you have any questions or concerns.
            </p>
          </div>
          {/* 2nd column */}
          <div className="footer-subscribe">
            
          </div>
          {/* 3rd column */}
          <div className="footer-social">
            <h3>Follow US</h3>
            <div className="footer-social--icons">
              <div>
                <a href="" target="_blank">
                  <FaDiscord className="icons" />
                </a>
              </div>
              <div>
                <a
                  href="https://www.instagram.com/ashi198patel/"
                  target="_blank"
                >
                  <FaInstagram className="icons" />
                </a>
              </div>
              <div>
                <a
                  href="https://www.linkedin.com/in/ashish-patel-861225220/"
                  target="_blank"
                >
                  <FaLinkedin className="icons" />
                </a>
              </div>
            </div>
          </div>
          {/* 4th column  */}
          <div className="footer-contact">
            <h3>Call Us</h3>
            <h3>+91 9837938302</h3>
          </div>
        </div>
        <div className="footer-bottom--section">
          <hr />
          <div className="container grid grid-two-column">
            <p>@{new Date().getFullYear()} Medistats. All Rights Reserved</p>
            <div>
              <p>PRIVACY POLICY</p>
              <p>TERMS & CONDITIONS</p>
            </div>
          </div>
        </div>
      </footer>
    </Wrapper>
  );
};
const Wrapper = styled.section`
  
`;
export default Footer;
