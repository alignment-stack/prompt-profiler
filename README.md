Prompt Profiler

A simple CLI tool to measure how efficient your AI prompts are through token usage, redundancy, and entropy metrics. It can be used with an offline LLM local to your machine, OpenAI API, or mock mode. 

You can run the profiler using any Hugging Face CasualLM from the terminal:

  python prompt-profiler.py "prompt text here" --model "gpt2"

OR

  python prompt_profiler.py "Prompt text here" --mode local --model_path /models/model

FEATURES
- Token counts (prompt & response)
- word/character stats
- Redundancy & entropy scores
- Efficiency rating
- local LLM, OpenAI API, or mock mode.

  *optional for OpenAI integration:
    pip install openai tiktoken

INTERACTIVE MODE

From within the folder run "python prompt_profiler.py". This will launch the terminal and ask you to enter in a model or path. It will then ask you to enter in your prompt. The response will be your test results. 

DEPENDENCIES
Please make sure you have the following installed prior to running the tool:
- torch
- transformers
- nltk
- rich

SAMPLE OUTPUT:

<pre><i>                                                                                  Prompt Profiler Results                                                                                    </i>
╭───────────────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│<b> Metric                    </b>│<b> Value                                                                                                                                                          </b>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Model                     </b></font>│<font color="#2AA1B3"><b> gpt2                                                                                                                                                           </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Device                    </b></font>│<font color="#2AA1B3"><b> cpu                                                                                                                                                            </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt                    </b></font>│<font color="#2AA1B3"><b> what is a tree?                                                                                                                                                </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Latency (s)               </b></font>│<font color="#2AA1B3"><b> 3.389                                                                                                                                                          </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output                    </b></font>│<font color="#2AA1B3"><b> How does it look when you&apos;re standing on the ground, with your feet up?&quot;                                                                                       </b></font>│
│<font color="#A347BA"><b>                           </b></font>│<font color="#2AA1B3"><b>  &quot;A natural forest. It&apos;s not like any of us have ever lived here,&quot; said Harry as he pulled out his trunk and opened its lid: green leaves that resembled       </b></font>│
│<font color="#A347BA"><b>                           </b></font>│<font color="#2AA1B3"><b> tresses stretching across an open field; white branches twitching to life in their new home beneath trees whose roots had been cut down by war-torn enemies    </b></font>│
│<font color="#A347BA"><b>                           </b></font>│<font color="#2AA1B3"><b> (and now only through good fortune); one single leaf was still hanging from something about                                                                    </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Token Count        </b></font>│<font color="#2AA1B3"><b> 5                                                                                                                                                              </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Char Count         </b></font>│<font color="#2AA1B3"><b> 15                                                                                                                                                             </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Unique Word Count  </b></font>│<font color="#2AA1B3"><b> 5                                                                                                                                                              </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Redundancy Percent </b></font>│<font color="#2AA1B3"><b> 0.0                                                                                                                                                            </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Entropy            </b></font>│<font color="#2AA1B3"><b> 2.322                                                                                                                                                          </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Prompt Efficiency         </b></font>│<font color="#2AA1B3"><b> 1.51                                                                                                                                                           </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Token Count        </b></font>│<font color="#2AA1B3"><b> 103                                                                                                                                                            </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Char Count         </b></font>│<font color="#2AA1B3"><b> 489                                                                                                                                                            </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Unique Word Count  </b></font>│<font color="#2AA1B3"><b> 98                                                                                                                                                             </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Redundancy Percent </b></font>│<font color="#2AA1B3"><b> 4.85                                                                                                                                                           </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Entropy            </b></font>│<font color="#2AA1B3"><b> 6.589                                                                                                                                                          </b></font>│
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│<font color="#A347BA"><b> Output Efficiency         </b></font>│<font color="#2AA1B3"><b> 13.57                                                                                                                               </b></font></pre>
