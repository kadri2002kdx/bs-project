// js/firebase-config.js
import { initializeApp, getApps } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js";
import { getAuth, setPersistence, browserLocalPersistence, onIdTokenChanged } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-auth.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-database.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-storage.js";


// === استبدل إذا لزم الأمر بالقيم الخاصة بمشروعك، لكن هذه القيم تعمل إذا كان مشروعك ecoplant-dz ===
const firebaseConfig = {
apiKey: "AIzaSyCVELN-Jca7q3xtS0uWk2ZrNnlqXJzsKpg",
authDomain: "ecoplant-dz-148bf.firebaseapp.com",
databaseURL: "https://ecoplant-dz-148bf-default-rtdb.europe-west1.firebasedatabase.app",
projectId: "ecoplant-dz-148bf",
storageBucket: "ecoplant-dz-148bf.appspot.com",
messagingSenderId: "233372376001",
appId: "1:233372376001:web:2c261f4bf161a65f726d40",
measurementId: "G-4PJZMLMKJE"
};


const app = getApps().length ? getApps()[0] : initializeApp(firebaseConfig);
const auth = getAuth(app);
await setPersistence(auth, browserLocalPersistence); // جلسة محلية (تبقى بعد إعادة تحميل)
const db = getDatabase(app);
const storage = getStorage(app);


// مراقب يحاول تجديد التوكن؛ إن فشل (مثلاً: الحساب محذوف في الكونسول) سيتم تسجيل الخروج تلقائياً
onIdTokenChanged(auth, async (user) => {
if (!user) return;
try {
await user.getIdToken(true);
} catch (e) {
console.warn("Auth token invalid — signing out:", e);
try { await auth.signOut(); } catch {}
localStorage.clear();
window.location.href = "login.html";
}
});


export { app, auth, db, storage };