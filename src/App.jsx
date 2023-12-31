import { useReducer } from 'react';
import Header from './components/header/Header';
import About from './components/about/About';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import ProductItem from './components/ProductItem';
import ShoppingCartProduct from './components/ShoppingCartProduct';
import { reducerCart, productsInitialState } from './reducers/shoppingCart_reducer';
import TYPES from './reducers/actionTypes';

function App() {

  const [state, dispatch] = useReducer(reducerCart, productsInitialState);

  const addToCart = (id) => {
    dispatch({
      type: TYPES.ADD_TO_CART,
      payload: id
    })
  }

  const deleteFromCart = (id) => {
    dispatch({
      type: TYPES.DELETE_PRODUCT_FROM_CART,
      payload: id
    })
  }

  const clearCart = () => {
    dispatch({
      type: TYPES.DELETE_ALL_FROM_CART
    })
  }

  const calculateTotalPriceOfCart = () => {
    dispatch({ type: TYPES.CALCULATE_TOTAL_PRICE_OF_THE_CART })
  }


  return (
    <>
    <Header/>
      <h1 className='title'>Productos en Disponibles</h1>
      <hr />
      <div className='container_grid_products'>
        {
          state.products.map((product) => {
            return <ProductItem key={product.id} data={product} addToCart={addToCart} />
          })
        }
      </div>

      <hr />
      <h2 className='subtitle_shopping_cart'>Carro de Compra</h2>
      <div className='container_buttons'>
        <button className='btn btn_totalPrice' onClick={() => calculateTotalPriceOfCart()}>Precio Total</button>
        {state.totalPriceShoppingCart > 0 && <p className='totalPrice_shoppingCart'>Precio Total: {state.totalPriceShoppingCart}</p>}
        <button className='btn btn_ClearCart' onClick={() => clearCart()}>Vaciar</button>
      </div>
      {
        state.cart.length === 0 && <p className='text_NoProductsInCart'>No hay productos en el carrito</p>
      }

      <div className='container_grid_shopping_cart'>


        {
          state.cart.map((productCart) => {
            return <ShoppingCartProduct key={productCart.id + (Math.random() * 50)} data={productCart} deleteFromCart={deleteFromCart} />
          })
        }
      </div>
      <About/>
    </>
  )
}

export default App
