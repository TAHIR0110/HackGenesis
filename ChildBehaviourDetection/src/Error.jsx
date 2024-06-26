import React from 'react'
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';
import { Button } from './styles/button';
const Error = () => {
  return (
    <Wrapper>
        <img src='../images/error.svg' alt='error'/>
        <NavLink to='/'>
        <Button className='btn'>Go back</Button>
        </NavLink>
    </Wrapper>
  )
}

const Wrapper = styled.section`
padding:9rem 0;
display:flex;
justify-content:center;
align-items:center;
flex-direction:column;

.btn{
    font-size:1.8rem;
    margin-top:3rem;
}
`;
export default Error