
import React from "react";
import styled from "styled-components";
import './Services.scss'
// import { useGlobalContext } from "./context";
// import { NavLink } from "react-router-dom";
import { Button } from "./styles/Button";
import Dl from "../src/images/images/p-1.jpg";
import Ad from "../src/images/images/p-2.jpg";
import Di from "../src/images/images/p-3.jpg";
import Do from "../src/images/images/p-4.jpg";
import D from "../src/images/images/p-5.jpg";
const getServices = [
  {
    id: "01",
    title: "Dyslexia",
    imgUrl: Dl,
    url: "../courses/Dyslexia/index.html",
  },
  {
    id: "02",
    title: "ADHD",
    imgUrl: Ad,

    url: "../courses/ADHD/index.html",
  },

  {
    id: "03",
    title: "Autism",
    imgUrl: Di,
    url: "../courses/Autism/index.html",
  },

  {
    id: "04",
    title: "Not Sure What Kind Of Care You Need?",
    imgUrl: Do,

    url: "",
  },
];

const Services = () => {
  return (
    <Wrapper className="section">
      <h2 className="common-heading">What Is Your Child Struggling With?</h2>
      <div className="container grid grid-three-column">
        {getServices.map((curElem) => {
          const { id, title, imgUrl } = curElem;
          return (
            <div key={id} className="card">
              <figure>
                <img src={imgUrl} alt="#" />
              </figure>
              <div className="card-data">
                <h3>{title}</h3>
                <Button className="btn">
                  <a href={curElem.url} target="_blank" className="btn-in">
                    Take Test
                  </a>
                </Button>
              </div>
            </div>
          );
        })}
      </div>
    </Wrapper>
  );
};

const Wrapper = styled.section`
 
`;

export default Services;
