<template>
  <div class="q-pa-md">
    <q-card class="leaders">
      <q-list bordered>
        <q-item-label header>Таблица лидеров групп</q-item-label>

        <q-item
          v-for="(contact, id) in offline"
          :key="id"
          class="q-mb-sm"
          clickable
          v-ripple
        >
          <q-item-section>
            <q-item-label>{{ contact.name }}</q-item-label>
            <q-item-label caption lines="1"
              >{{ contact.points }} Баллов -
              {{ contact.percentage }} %</q-item-label
            >
          </q-item-section>

          <q-item-section side>
            <div class="row">
              <span class="q-mr-sm">{{ id + 1 }}</span>
              <img
                v-if="contact.status === 'up'"
                src="../../assets/result/GeneralStatistics/arrawUp.png"
                alt=""
                class="icon"
              />
              <img
                v-if="contact.status === 'down'"
                src="../../assets/result/GeneralStatistics/arrow_down.png"
                alt=""
                class="icon"
              />
            </div>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>
  </div>
</template>

<script setup>
const offline = [
  {
    id: 1,
    name: "5 Управление",
    points: 785,
    percentage: 92,
    avatar: "avatar1.jpg",
    status: "up",
  },
  {
    id: 2,
    name: "12 Департамент",
    points: 654,
    percentage: 87,
    avatar: "avatar2.jpg",
    status: "down",
  },
  {
    id: 3,
    name: "3 Управление",
    points: 710,
    percentage: 89,
    avatar: "avatar3.jpg",
    status: "up",
  },
  {
    id: 4,
    name: "10 Управление",
    points: 670,
    percentage: 90,
    avatar: "avatar4.jpg",
    status: "up",
  },
  {
    id: 5,
    name: "7 Управление",
    points: 623,
    percentage: 85,
    avatar: "avatar5.jpg",
    status: "down",
  },
];
</script>

<style scoped>
.leaders {
  padding: 12px;
  border-radius: 10px;
}

.icon {
  width: 20px;
}
</style>
