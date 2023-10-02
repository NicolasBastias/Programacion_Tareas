import React from 'react'
import styles from '../styles/ProductItem.module.css';
export default function ProductoItem({ data, addToCart }) {
  return (
    <div className={styles.container_product}>
      <h2>{data.name}</h2>
      <p>Precio: {data.price}</p>
      <img src={data.image} alt={data.name} />
      <button className={styles.btnProduct} onClick={() => addToCart(data.id)}>Agregar al Carro</button>
    </div>
  )
}
