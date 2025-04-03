<template>
  <div>
    <input type="file" @change="handleFileUpload" accept="image/*" />
    <button @click="uploadFile">Upload Image</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedFile = ref(null)
const imageData = ref(null)

const handleFileUpload = (event) => {
  selectedFile.value = event.target.files[0]
  if (selectedFile.value) {
    const reader = new FileReader()
    reader.onload = (e) => {
      imageData.value = e.target.result
    }
    reader.readAsArrayBuffer(selectedFile.value)
  }
}

const uploadFile = async () => {
  if (!imageData.value) return

  try {
    const response = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/octet-stream',
        'Content-Disposition': `attachment; filename="${selectedFile.value.name}"`,
      },
      body: imageData.value,
    })
    const result = await response.json()
    console.log(result)
  } catch (error) {
    console.error('Error uploading image:', error)
  }
}
</script>
