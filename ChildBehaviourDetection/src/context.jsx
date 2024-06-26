import React, { useContext, useReducer, useEffect } from "react";
import reducer from "./reducer";
import axios from "axios";
const AppContext = React.createContext();
import './context.css'

const initialState = {
  name: "",
  image: "",
  services: [],
};

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);


  const updateHomePage = () => {
    return dispatch({
      type: "HOME_UPDATE",
      payload: {
        class:"Image",
        name: "KhoJo.",
        image: "../public/images/hero.jpg",
      },
    });
  };

  const updateAboutPage = () => {
    return dispatch({
      type: "ABOUT_UPDATE",
      payload: {
        name: "Tanjul Sarathe",
        image: "./images/about1.svg",
      },
    });
  };

  // to call the api
  useEffect(() => {
    // getServices();
  }, []);

  return (
    <AppContext.Provider value={{ ...state, updateHomePage,updateAboutPage}}>
      {children}
    </AppContext.Provider>
  );
};

// global custom hook
const useGlobalContext = () => {
  return useContext(AppContext);
};

export { AppProvider, useGlobalContext };