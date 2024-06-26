import React from "react";
import { NavLink } from "react-router-dom";
// import styled from "styled-components";
import { Button } from "../styles/button";
import { useGlobalContext } from "../context";
import "./HeroSection.css";

const HeroSection = () => {
  const { name, image } = useGlobalContext();
  return (
   
      <div className="container grid grid-two-column">
        <div className="section-hero-data">
          <h1 className="hero-heading">Trust Medistats with your mental health</h1>
          <p className="hero-para">
            Our mission is simple: to help you feel better, get better and stay
            better. We bring together self-care, professional support, and
            community access to deliver the best quality mental healthcare for
            your needs.
          </p>
          <Button className="btnn">
            <NavLink to="/contact">Start Now</NavLink>
          </Button>
        </div>

        <div className="section-hero-image">
          <picture>
            <img src={image} alt="hero image" className="hero-img" />
          </picture>
        </div>
      </div>
    
  );
};
// const Wrapper = styled.section``;

export default HeroSection;
