/*funcion reducer */
import TYPES from "./actionTypes";

export const productsInitialState = {
  products: [
    {
      "id": 1,
      "name": "product 1",
      "price": 50,
      "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.firsttothefinish.com%2Fmobile%2FItemMatrix.asp%3FCc%3Dfw_pvault_spike%26GroupCode%3DAA1204%252D003%26eq%3Dfw_AA1204003%26MatrixType%3D1&psig=AOvVaw2m1Jl9QgqtSpyqACO0zhGi&ust=1696306503832000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKjX2abA1oEDFQAAAAAdAAAAABAH"
    },
    {
      "id": 2,
      "name": "product 2",
      "price": 30
    },
    {
      "id": 3,
      "name": "product 3",
      "price": 40
    },
    {
      "id": 4,
      "name": "product 4",
      "price": 78
    },
    {
      "id": 5,
      "name": "product 5",
      "price": 90
    },
    {
      "id": 6,
      "name": "product 6",
      "price": 60
    }
  ],
  cart: [],
  totalPriceShoppingCart: 0
}

export const reducerCart = (state, action) => {
  switch (action.type) {
    case TYPES.ADD_TO_CART: {
      let newProduct = state.products.find((product) => product.id === action.payload)
      return {
        ...state,
        cart: [...state.cart, newProduct]
      };
    }
    case TYPES.DELETE_PRODUCT_FROM_CART: {
      return {
        ...state,
        cart: state.cart.filter((product) => product.id !== action.payload)
      }
    }

    case TYPES.DELETE_ALL_FROM_CART: {
      return productsInitialState;
    }

    case TYPES.CALCULATE_TOTAL_PRICE_OF_THE_CART: {
      return {
        ...state,
        totalPriceShoppingCart: state.cart.reduce((previousValue, product) => previousValue + product.price, 0)
      }
    }
    default:
      return state;
  }

  throw Error("Unknown action: " + action.type);
}