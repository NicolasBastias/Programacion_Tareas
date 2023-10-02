import React from 'react';
import "./header.css";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
// import LoginRegistro from './LoginRegistro';
import NavDropdown from 'react-bootstrap/NavDropdown';
const Header = () => {
  return (
    <div>


      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">Banana/Shop</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <Nav.Link href="#home">Home</Nav.Link>
            </Nav>
            <div className="navbar-divider"></div>
            <Nav className="navbar-nav">
              <Nav.Link href="#login">Login</Nav.Link>
              <Nav.Link href="#registro">Registro</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>


    </div>
  )
}

export default Header
