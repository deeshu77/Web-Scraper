<template>
  <div>
    <h2>HTML Inspector</h2>
    <iframe
      id="preview"
      ref="iframe"
      sandbox="allow-same-origin allow-scripts"
      style="width: 100%; height: 400px; border: 1px solid #ccc;"
    ></iframe>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'

// Define the emit function
const emit = defineEmits(['update:selected'])

const selected = ref([])
const iframe = ref(null)

// Accept htmlContent as a prop
const props = defineProps({
  htmlContent: String
})

// Watch for changes in htmlContent prop and inject the content into iframe
watch(() => props.htmlContent, (newHtmlContent) => {
  if (newHtmlContent) {
    loadHTML(newHtmlContent)
  }
}, { immediate: true })

const loadHTML = (htmlContent) => {
  try {
    // Ensure the iframe is fully loaded before writing content
    nextTick(() => {
      const doc = iframe.value.contentDocument
      doc.open()
      doc.write(htmlContent)
      doc.close()

      injectInspector(doc)  // Call the function to enable the inspector
    })
  } catch (error) {
    console.error('Error loading HTML content into iframe:', error)
  }
}

const injectInspector = (doc) => {
  const style = doc.createElement('style')
  style.innerHTML = `
    .hover-highlight {
      outline: 2px dashed red !important;
      cursor: pointer !important;
    }
    .selected-element {
      outline: 3px solid green !important;
      background-color: rgba(0, 255, 0, 0.1) !important;
      position: relative;
    }
    .selected-element::after {
      content: "Selected";
      position: absolute;
      top: -1.5em;
      left: 0;
      background: green;
      color: white;
      padding: 2px 5px;
      font-size: 10px;
      font-family: sans-serif;
    }
  `
  doc.head.appendChild(style)

  // Hover event to highlight elements
  doc.body.addEventListener('mouseover', e => {
    e.stopPropagation()
    doc.querySelectorAll('.hover-highlight').forEach(el => el.classList.remove('hover-highlight'))
    e.target.classList.add('hover-highlight')
  }, true)

  // Mouseout event to remove hover highlight
  doc.body.addEventListener('mouseout', e => {
    e.stopPropagation()
    e.target.classList.remove('hover-highlight')
  }, true)

  // Click event to select the element and emit the selected components
  doc.body.addEventListener('click', async e => {
    e.preventDefault()
    e.stopPropagation()

    const html = e.target.outerHTML
    if (!selected.value.includes(html)) {
      e.target.classList.add('selected-element')
      selected.value.push(html)

      // Emit the selected element to the parent
      emit('update:selected', selected.value)
    }
  }, true)
}
</script>

<style>
iframe {
  width: 100%;
  height: 500px;
  border: 1px solid #ccc;
}
</style>
