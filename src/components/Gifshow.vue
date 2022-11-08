<script setup>
defineProps({
  link: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="contain">
    <img :src="link" alt="Image">
  </div>
</template>