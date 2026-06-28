<template>
  <section>
    <table>
      <thead>
        <tr>
          <th v-for="head in headers" :key="head">{{ head }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in items" :key="row.id">
          <td v-for="cell in row" :key="cell">{{ cell }}</td>
          <td v-if="acciones">
            <button class="btn btn-primary" @click="$emit('editar', row[0])">
              <mdicon name="pencil"></mdicon> Editar
            </button>
            <button class="btn btn-danger" @click="$emit('eliminar', row[0])">
              <mdicon name="trash-can"></mdicon> Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
import { computed } from "vue";
const props = defineProps({
  headers: {
    type: Array,
    required: true,
  },
  data: {
    type: Array,
    required: true,
  },
  acciones: {
    type: Boolean,
    default: true,
  },
});

const items = computed(() => {
  if (props.data.length === 0) {
    return [];
  }
  const values = props.data.map((item) => {
    const row = [];
    for (const key in item) {
      if (props.headers.includes(key.toUpperCase())) {
        row[props.headers.indexOf(key.toUpperCase())] = item[key];
      }
    }
    return row;
  });
  return values;
});
</script>

<style scoped>
table {
  margin: 0 auto;
  width: 70%;
  border-collapse: collapse;
}
th {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}
td {
  text-align: center;
  padding: 8px;
}
.btn {
  background-color: #0b7b8d;
  border: none;
  color: #fff;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 5px;
  margin: 0 5px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.btn:hover {
  background-color: #0a6a7b;
}
.btn-danger {
  background-color: #d9534f;
}
.btn-danger:hover {
  background-color: #c9302c;
}
</style>
