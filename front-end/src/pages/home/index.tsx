import { useEffect, useState } from "react";
import "./index.sass";
import GetResumo from "../../services/getResumo";
import GetCompare from "../../services/getCompare";

export default function Home() {
  const [type, setType] = useState<number>(1);
  const [file1, setFile] = useState<File | null>();
  const [file2, setFile2] = useState<File | null>();
  const [question, setQuestion] = useState<string>("");
  const [data, setData] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [file1Warning, setFile1Warning] = useState<boolean>(false);
  const [file2Warning, setFile2Warning] = useState<boolean>(false);
  const [isFullReport, setIsFullReport] = useState<boolean>(false);
  const [questionDisabled, setQuestionDisabled] = useState<boolean>(false);

  const handleCopyToClipboard = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
  
    if (data) {
      const tempTextArea = document.createElement("textarea");
      tempTextArea.value = data;
      document.body.appendChild(tempTextArea);
      tempTextArea.select();
      document.execCommand("copy");
      document.body.removeChild(tempTextArea);
    }
  };

  async function submitAndGetExcel(
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) {
    e.preventDefault();
    setLoading(true);

    try {
      let finalQuestion = question
      if(isFullReport){
        finalQuestion += "Com base no texto, extraia em tópicos se houver o(s): 1. CNPJ; 2. endereço de faturamento e de instalação; 3. produto contratado, cadastro do cliente (nome/razão social); 4. valor do contrato/aditivo mensal e taxa de instalação; 5. cliente possui descontos especiais; 6. Cliente governo tem retenção de impostos; 7. Data de assinatura do contrato; 8. Indice de reajuste do cliente; 9. periodo de reajuste do contrato do cliente; 10. Data base do cliente; 11. Renovação contratual; 12. houve isenção da taxa de instalação; 13. cliente governo possui contrato de licitação anexado; 14. se existe muilta contratual em caso de rescisão e o percentual."
      }

      if (type == 1 && file1) {
        setFile1Warning(false);
        const response = await GetResumo(file1, finalQuestion);
        setData(response);
      } else if (type == 2 && file1 && file2) {
        setFile1Warning(false);
        setFile2Warning(false);
        const response = await GetCompare(file1, file2);
        setData(response);
      } else {
        setFile1Warning(!file1)
        setFile2Warning(type === 2 && !file2)
      }
    } catch (error) {
      console.error("Ocorreu um erro:", error);
    } finally {
      setLoading(false);
    }
  }

  const SetFiles = (
    e: React.ChangeEvent<HTMLInputElement>,
    setFunction: React.Dispatch<React.SetStateAction<File | null | undefined>>,
    setWarning: React.Dispatch<React.SetStateAction<boolean>>
  ) => {
    if (e.target.files && e.target.files.length > 0) {
      const selectedFile = e.target.files[0];

      const allowedExtensions = /(\.pdf|\.mp4|\.wav)$/i;
      
      if (!allowedExtensions.exec(selectedFile.name)){
        setWarning(true);
        setFunction(null);
        window.alert("Selecione apenas arquivos em formato PDF ou arquivos de audio (mp4 ou wav)!");
      } else {
        setWarning(false);
        setFunction(selectedFile);
      }   
    }
  };

  return (
    <div className="formDiv">
      <div className="content">
        <form action="" className="FormTime">
        <div className="titleGeneral">
            <div className="titleDataExplorer">
              <img src="/images/logo-algar-telecom.png" alt="" />
            </div>
            <h1>Comparação ou análise/resumo de arquivos. </h1>
          </div>
          <div className="timeInput">
            <label htmlFor="time"><b>Tipo:</b></label>
            <select
              name="time"
              onChange={(e) => setType(Number(e.target.value))}
              value={type}
            >
              <option value="1">Analisar / Resumo </option>
              <option value="2">Comparar</option>
            </select>
          </div>
          <div className="mailInput">
            <label htmlFor="email">
              <b>Coloque o seu arquivo aqui:</b>
              <br />*apenas arquivos em formato .pdf ou audio (.mp4 ou .wav).
            </label>
            <input
              type="file"
              name="file1"
              id="file1"
              onChange={(e) => SetFiles(e, setFile, setFile1Warning)}
            />
          </div>
          {type !== 1 ? (
            <>
              {" "}
              <div className="mailInput">
                <label htmlFor="file2">
                  <b>Coloque o seu segundo arquivo aqui para comparação com o de cima:</b>
                  <br />*apenas arquivos em formato .pdf ou audio (.mp4 ou .wav).
                </label>
                <input
                  type="file"
                  name="file2"
                  id="file2"
                  onChange={(e) => SetFiles(e, setFile2, setFile2Warning)}
                />
              </div>
            </>
          ) : (
            ""
          )}
          {type == 1 ? (
            <>
              {" "}
              <div className="questionInput">
                <label htmlFor="question"><b>Coloque sua pergunta:</b></label>
                <input
                  type="text"
                  name="question"
                  id="question"
                  onChange={(e) => setQuestion(e.target.value)}
                  value={question}
                  disabled={questionDisabled}
                />
              </div>
              ou
              <div className="creativeInput">
                <label htmlFor="creative">
                  <input
                    type="checkbox"
                    name="creative"
                    id="creative"
                    onChange={() => {
                      setIsFullReport(!isFullReport);
                      setQuestionDisabled(!isFullReport);
                    }}
                  />
                  Relatório Completo.
                </label>
              </div>
            </>
          ) : (
            ""
          )}
          <div className="buttonWithLoading">
            <button
              type="button"
              disabled={loading}
              onClick={(e) => submitAndGetExcel(e)}
            >
              Comparar/Analisar
            </button>
            {loading ? <span className="loader"></span> : ""}
          </div>          
        </form>
      </div>
      <div className="certopsBG">
              
                <p>A resposta aparecerá logo abaixo:</p>
                {data && !loading ? (
                <>
                {data}
                <br />
                <br />
                <button className="copy-button" onClick={handleCopyToClipboard}>
                  Copiar
                </button>
                </>
                ) : (
                ""
                )}              
              
      </div>
    </div>
  );
}
