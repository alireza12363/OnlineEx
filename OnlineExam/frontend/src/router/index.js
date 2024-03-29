import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import TheExam from "../components/exam_components/TheExam.vue"
import FinishPage from "../views/FinishPage.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  
  {
    path: "/:SessionId",
    name: "Exam",
    component: TheExam,
  },
  {
    path: "/finish-:SessionId",
    name: "FinishPage",
    component: FinishPage,
  },

 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
