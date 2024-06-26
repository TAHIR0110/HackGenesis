import React from "react";
import styled from "styled-components";
import "./Contact.scss";

const Contact = () => {
  const Wrapper = styled.section``;
  return (
    <Wrapper>
      <h2 className="common-heading"> Send Your Query </h2>

      <div className="container">
        <div className="contact-form">
          <form
            action="https://formspree.io/f/mgebabpd"
            method="POST"
            className="contact-inputs"
          >
            <input
              type="text"
              name="username"
              className="radius"
              placeholder="username"
              autoComplete="off"
              required
            />

            <input
              type="email"
              name="Email"
              className="radius"
              placeholder="Email"
              autoComplete="off"
              required="true"
            />
            <textarea
              name="message"
              cols="30"
              className="radius"
              rows="6"
              placeholder="Write your message here"
              autoComplete="off"
              required
            ></textarea>
            <input type="submit" value="send" />
          </form>
        </div>
      </div>
    </Wrapper>
  );
};

export default Contact;
