// js/cloudinary.js
export async function uploadToCloudinary(file) {
if (!file) throw new Error('No file provided');
const formData = new FormData();
formData.append('file', file);
formData.append('upload_preset', 'unsigned_preset'); // preset اللي أنشأته


const res = await fetch('https://api.cloudinary.com/v1_1/dq5cgwwjt/image/upload', {
method: 'POST',
body: formData
});
const data = await res.json();
if (!res.ok) throw new Error(data.error?.message || 'Cloudinary upload failed');
return data; // يحتوي secure_url
}