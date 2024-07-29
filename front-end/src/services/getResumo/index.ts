import {env} from "../baseUrl";

interface Props {
  question: string;
  file1: File;
}

export default async function GetResumo(file1: File, question: string) {
  
  const formData = new FormData();
  formData.append('file1', file1, file1.name);
  formData.append('question', question);

  // const response = await baseUrlGlobal.post('/getResumo', formData, {headers:{"Content-Type": "multipart/form-data"}});

  try {
    const response = await fetch(env.local.concat('/getResumo'), {
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