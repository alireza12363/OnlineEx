<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light custom-nav">
        <div class="container">
            <span class="navbar-brand">Online Exam System</span>

            <ul class="navbar-nav ml-auto">
                <li v-if="page == 'Exam'" >
                    <div v-if="duration > 0">
                        <exam-timer :exam_dur="duration" />
                    </div>
                </li>

                <li class="nav-item active">
                    <p>
                        <span class="badge badge-light">{{ user["first_name"] }} {{ user['last_name'] }}</span>
                    </p>
                </li>
                <li v-if="page == 'Home' || page == 'Finish'" class="nav-item">
                    <a class="btn btn-sm btn-danger"
                        href="/accounts/logout/"
                        tabindex="-1"
                        >Logout</a>
                </li>
                <li v-else-if="page == 'Exam'">
                    <a class="btn btn-sm btn-danger"
                        tabindex="-1"
                        @click="$emit('click-quit')"
                        >Quit the Exam</a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
import { apiService } from "../../common/api.service";
import ExamTimer from '../exam_components/ExamTimer.vue';

export default {
    components: { ExamTimer },
    name: "NavbarComponent",

    data() {
        return {
            user: {},
            time: null
        };
    },

    props: ['page', 'duration'],

    methods: {
        getUserData() {
            let endpoint = "api/rest-auth/user/";
            console.log(endpoint);
            apiService(endpoint).then((data) => {
                console.log(data);
                this.user = JSON.parse(JSON.stringify(data));
            });
        },
    },

    mounted() {
        this.getUserData();
    },
};
</script>

<style scoped>
.custom-nav {
    border-bottom: 1px solid #ddd;
}
</style>
