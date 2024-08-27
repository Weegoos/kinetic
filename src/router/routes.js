const routes = [
  {
    path: "/",
    component: () => import("../pages/IndexPage.vue"),
  },
  {
    path: "/class_calendar",
    component: () => import("../pages/ClassCalendar.vue"),
  },
  {
    path: "/event_calendar",
    component: () => import("../pages/EventCalendar.vue"),
  },
  {
    path: "/result",
    component: () => import("../pages/ResultPage.vue"),
  },
  {
    path: "/analytics",
    component: () => import("../pages/AnalyticsPage.vue"),
  },
  {
    path: "/staff",
    component: () => import("../pages/StaffPage.vue"),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
