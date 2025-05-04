<template>
  <div>
    <!-- ScraperChild component emits selected components -->
    <ScraperChild :htmlContent="htmlContent" @update:selected="handleSelected" />
    
    <div style="margin-top: 20px;">
      <h3>Selected Elements:</h3>
      <ul>
        <li v-for="(item, index) in selected" :key="index">
          <pre>{{ item }}</pre>
          <span class="remove" @click="removeSelected(index)">×</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ScraperChild from './ScraperChild.vue' // Import ScraperChild component

const props = defineProps({
  htmlContent: String
})
// Array to store the selected components
const selected = ref([])

// Handle the updated selected components emitted by ScraperChild
const handleSelected = (newSelected) => {
  selected.value = newSelected
}

const removeSelected = (index) => {
  selected.value.splice(index, 1) 
} // Removes the element at the given index
</script>

<style scoped>
.remove {
  color: red;
  font-size: 20px;
  cursor: pointer;
  margin-left: 10px;
}

.remove:hover {
  color: darkred;
}
</style>


