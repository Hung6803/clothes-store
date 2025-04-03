import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const selectedProducts = ref([])

  // Thêm sản phẩm vào giỏ hàng
  const addProduct = (product) => {
    const index = selectedProducts.value.findIndex((p) => p.id === product.id)
    if (index === -1) {
      selectedProducts.value.push({ ...product})
    } else {
      selectedProducts.value[index].quantity += product.quantity
    }
  }

  // Xóa sản phẩm khỏi giỏ hàng
  const removeProduct = (productId) => {
    selectedProducts.value = selectedProducts.value.filter((p) => p.id !== productId)
  }

  // Tăng giảm số lượng sản phẩm
  const updateQuantity = (productId, quantity) => {
    const index = selectedProducts.value.findIndex((p) => p.id === productId)
    if (index !== -1) {
      if (selectedProducts.value[index].total_quantity >= quantity) {
        selectedProducts.value[index].quantity = quantity > 0 ? quantity : 1
      }
    }
  }

  // Tính tổng số lượng sản phẩm
  const totalItems = computed(() =>
    selectedProducts.value.reduce((total, p) => total + p.quantity, 0)
  )

  const totalPrice = computed(() =>
    selectedProducts.value.reduce((sum, p) => {
      const finalPrice = p.discount > 0 ? p.price * (1 - p.discount / 100) : p.price
      return sum + p.quantity * finalPrice
    }, 0)
  )

  return { selectedProducts, addProduct, removeProduct, updateQuantity, totalItems, totalPrice }
})