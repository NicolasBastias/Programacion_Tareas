import React from 'react';
import "./loginregistro.css";
import Nav from 'react-bootstrap/Nav';

const LoginRegistro = () => {
  return (
    <Nav>
      <Nav.Link href="#login">Login</Nav.Link>
      <Nav.Link href="#registro">/</Nav.Link>
      <Nav.Link href="#registro">Registro</Nav.Link>
    </Nav>
  );
};

export default LoginRegistro;

