import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const selectedProducts = ref([])

  // Thêm sản phẩm vào giỏ hàng
  const addProduct = (product) => {
    const index = selectedProducts.value.findIndex(
      (p) => p.id === product.id && p.size_id === product.size_id
    )
    if (index === -1) {
      selectedProducts.value.push({ ...product})
    } else {
      selectedProducts.value[index].quantity += product.quantity
    }
  }

  // Xóa sản phẩm khỏi giỏ hàng
  const removeProduct = (productId, sizeId) => {
    const index = selectedProducts.value.findIndex(
      (p) => p.id === productId && p.size_id === sizeId
    )
    if (index !== -1) {
      selectedProducts.value.splice(index, 1)
    }
  }

  // Tăng giảm số lượng sản phẩm
  const updateQuantity = (productId, sizeId, quantity) => {
    const index = selectedProducts.value.findIndex(
      (p) => p.id === productId && p.size_id === sizeId
    )
    if (index !== -1) {
      if (selectedProducts.value[index].total_quantity >= quantity) {
        selectedProducts.value[index].quantity = quantity > 0 ? quantity : 1
      }
    }
  }

  const updateSize = (productId, oldSizeId, newSizeId) => {
    const index = selectedProducts.value.findIndex(
        (p) => p.id === productId && p.size_id === oldSizeId)
    if (index !== -1) {
      const existingIndex = selectedProducts.value.findIndex(
        (p) => p.id === productId && p.size_id === newSizeId
      )

      // Nếu sản phẩm cùng size mới đã tồn tại → gộp số lượng
      if (existingIndex !== -1) {
        selectedProducts.value[existingIndex].quantity += selectedProducts.value[index].quantity
        selectedProducts.value.splice(index, 1)
      } else {
        selectedProducts.value[index].size_id = newSizeId
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

  return { selectedProducts, addProduct, removeProduct, updateQuantity, updateSize, totalItems, totalPrice }
})