<template>
    <div class="home">
        <navbar-component page='Home'/>
        <div class="container">
            <div v-if="ActiveSubSessions.length === 0  && ActiveCouSessions.length === 0">
                <h2 class="text text-primary">You have no active exams!</h2>
            </div>
            <div v-else>
                <h2>Your current exam session(s)</h2>
                <base-card
                    v-for="(session, ind) in ActiveSubSessions"
                    :key="ind"
                    class="container"
                >
                    Exam name (click to start):
                    <button
                        @click="startSession(session)"
                        class="btn btn-outline-success"
                    >
                        {{ session.session_name }}
                    </button>
                    <p>Exam Description: {{ session.session_descriptions }}</p>
                </base-card>
                <base-card
                    v-for="(session, ind) in ActiveCouSessions"
                    :key="ind"
                    class="container"
                >
                    Exam name (click to start):
                    <button
                        @click="startSession(session)"
                        class="btn btn-outline-success"
                    >
                        {{ session.session_name }}
                    </button>
                    <p>Exam Description: {{ session.session_descriptions }}</p>
                </base-card>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import NavbarComponent from "../components/UI/Navbar.vue";
import { apiService, postAxios } from "../common/api.service";
import BaseCard from "../components/UI/BaseCard.vue";

export default {
    components: { BaseCard, NavbarComponent },
    name: "Home",

    data() {
        return {
            ActiveSubSessions: [],
            ActiveCouSessions: [],
        };
    },

    methods: {
        getActiveSessions() {
            let endpoint = "api/sub-sessions/";
            apiService(endpoint).then((data) => {
                const midvar = [];
                midvar.push(...data);
                this.ActiveSubSessions = JSON.parse(JSON.stringify(midvar));
            });

            let endpoint_co = "api/cou-sessions/";
            apiService(endpoint_co).then((data) => {
                const midvar = [];
                midvar.push(...data);
                this.ActiveCouSessions = JSON.parse(JSON.stringify(midvar));
            });
        },
        startSession(session) {
            let endpoint = "api/results/";
            let data = {
                    "answers": null,
                    "is_finished": false,
                    "student": null,
                    "session_ref_number": session.session_ref_number
                };
            postAxios(endpoint, data).then( response => {
                console.log(response.data);
                this.$router.push({
                    name: "Exam",
                    params: { SessionId: session.session_ref_number },
                });
                }
            ).catch(e => {
                console.log(e);
            });
        },
    },

    mounted() {
        this.getActiveSessions();
    },
};
</script>
