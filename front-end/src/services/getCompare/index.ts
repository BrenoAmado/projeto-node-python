import {env} from "../baseUrl";

interface Props {
  file1: File;
  file2: File;
  }
  
export default async function GetCompare(file1: File, file2: File) {

  const formData = new FormData();
  formData.append('file1', file1, file1.name);
  formData.append('file2', file2, file2.name);
  
  // const response = await baseUrlGlobal.post('/getCompare', formData, {headers:{"Content-Type": "multipart/form-data"}});

  try {
    const response = await fetch(env.local.concat('/getCompare'), {
      method: 'POST',
      body: formData,
    });
  
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }
  
    const data = await response.text();
    return data;
  } catch (error) {
    console.error('Erro:', error);
    throw error;
  }
}