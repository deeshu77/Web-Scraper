<template>
  <div>
    <!-- ScraperParent receives selected components from ScraperChild -->
    <ScraperParent :htmlContent="htmlContent" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ScraperParent from './components/ScraperParent.vue'

const htmlContent = ref('')

onMounted(async () => {
  try {
    // Fetch the HTML content from the backend (Flask)
    const response = await axios.post('http://localhost:5000/fetch-html')
    console.log("Received HTML:", response.data);
    htmlContent.value = response.data.html

    // Pass htmlContent to ScraperChild through the parent component
    // ScraperParent is responsible for rendering selected elements
  } catch (error) {
    console.error('Error fetching HTML:', error)
  }
})
</script>
